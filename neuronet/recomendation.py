from web.models import Treatment, RecommendText
from neuronet.recomendation_text import *


def get_hunt_hess_by_treatment(treatment: Treatment) -> str:
    degree = 0
    if treatment.conscious_level == 15 and treatment.neurological_deficit == 1:
        degree = 1
    elif treatment.conscious_level == 15 and treatment.neurological_deficit == 2:
        degree = 2
    elif treatment.neurological_deficit == 3 and 11 <= treatment.conscious_level <= 14:
        degree = 3
    elif treatment.neurological_deficit == 4 and treatment.conscious_level == 9:
        degree = 4

    int_to_roman = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV'
    }
    # [7, 8, 9] - САК
    print(degree)
    # Fix treatment.predict.classification_types not in [7, 8, 9]
    return '' if (degree <= 0) or (treatment.predict.classification_types not in [7, 8, 9]) \
        else f'{int_to_roman[degree]} степень общей тяжести состояния по шкале Hunt Hess'


class VJK:
    def __init__(self, treatment: Treatment):
        self.recommendation_items = []
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        self.recommendation_items = [
            dynamic_observation,
            CT_in_dynamic_through_3_days,
            repeated_CT_and_consultation,
        ]


class VMG_VJK:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        if self.treatment.hematoma_volume:
            if self.treatment.hematoma_volume < 30:
                self.operation_text = low_operation_probability
                self.recommendation_items += [
                    conservative_therapy,
                    CT_angiography,
                    repeated_consultation_if_source_of_hemorrhage
                ]
            elif 30 < self.treatment.hematoma_volume < 60:
                if not self.treatment.temporary_contraindications and not self.treatment.patient.diagmnoses \
                        and int(self.treatment.conscious_level) >= 8:
                    self.operation_text = high_operation_probability
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
                else:
                    self.operation_text = high_operation_probability
                    self.recommendation_items += [
                        patient_has_contraindications_for_surgery,
                        dynamic_observation_if_abandonment_of_operation
                    ]
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
            else:
                self.operation_text = low_operation_probability_serious_condition_of_patient

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            CT_in_dynamic_through_3_days,
        ]
        return items


class VMG_posterior_fossa:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        if self.treatment.hematoma_volume:
            if self.treatment.hematoma_volume < 15:
                self.operation_text = low_operation_probability
                self.recommendation_items += [
                    conservative_therapy,
                    CT_angiography,
                    repeated_consultation_if_source_of_hemorrhage,
                ]
            elif 15 < self.treatment.hematoma_volume < 60:
                if not self.treatment.temporary_contraindications and not self.treatment.patient.diagmnoses:
                    self.operation_text = high_operation_probability
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
                else:
                    self.operation_text = high_operation_probability
                    self.recommendation_items += [
                        patient_has_contraindications_for_surgery,
                        dynamic_observation_if_abandonment_of_operation,
                    ]
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
            else:
                self.operation_text = low_operation_probability_serious_condition_of_patient

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            occlusive_hydrocephalus,
            CT_in_dynamic_through_3_days,
        ]
        return items


class VMG_conservative:
    def __init__(self, treatment: Treatment):
        self.recommendation_items = []
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        self.recommendation_items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            conservative_therapy,
            CT_angiography,
            repeated_consultation_if_source_of_hemorrhage,
        ]
        self.operation_text = low_operation_probability


class VMG_operation:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        if self.treatment.hematoma_volume:
            if 30 <= self.treatment.hematoma_volume <= 60:
                if not self.treatment.temporary_contraindications and not self.treatment.patient.diagmnoses \
                        and int(self.treatment.conscious_level) >= 8:
                    self.operation_text = high_operation_probability
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
                else:
                    self.operation_text = high_operation_probability
                    self.recommendation_items += [
                        patient_has_contraindications_for_surgery,
                        dynamic_observation_if_abandonment_of_operation,
                    ]
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
            else:
                self.operation_text = low_operation_probability_serious_condition_of_patient

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
        ]
        return items


class Ischemia_conservative:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        if self.treatment.time_passed:
            if self.treatment.time_passed <= 3.5:
                self.operation_text = 'Вероятность выполнения тромболизиса и тромбэкстракции высокая'
            elif 3.5 <= self.treatment.time_passed <= 12:
                self.operation_text = 'Вероятность выполнения тромболизиса низкая, есть вероятность решения вопроса в пользу тромбэкстракции'
            else:
                self.operation_text = 'Вероятность выполнения тромболизиса и тромбэкстракции низкая.'

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            'КТ-ангиография экстракраниальных и интракраниальных сосудов с целью выяснения уровня тромбоза и оценки коллатералей.',
            'КТ-перфузия с целью оценки зоны олигемии/некроза/пенумбры.',
            'Повторная консультация нейрохирурга. Решение вопроса о выполнении тромбинтимэктомии, ЭИКМА, ТЭ, КЭЭ, ТЛТ.'
        ]
        return items


class Ischemia_with_reperfusion:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        if self.treatment.hematoma_volume:
            if 30 <= self.treatment.hematoma_volume <= 60:
                self.operation_text = high_operation_probability

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            'КТ-ангиография экстракраниальных и интракраниальных сосудов с целью выяснения уровня тромбоза и оценки коллатералей.',
            'КТ-перфузия с целью оценки зоны олигемии/некроза/пенумбры.',
        ]
        return items


class Tumor:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        if int(self.treatment.conscious_level) <= 10:
            self.operation_text = 'Решение вопроса о выполнении оперативного лечения в неотложном порядке до выполнения МРТ головного мозга.'

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            'МРТ головного мозга с в/в контрастным усилением для исключения объемного процесса.',
            'Повторная консультация для решения вопроса об оперативном лечении.',
            'Консультация онколога.',
            'Онкопоиск: сбор онкоанамнеза, УЗИ брюшной полости КТ легких, УЗИ почек.'
        ]
        return items


class SAK:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        pass

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            CT_angiography,
            repeated_neurosurgeon_consultation,
            CT_in_dynamic_through_3_days,
        ]
        return items


class SAK_VMG:
    def __init__(self, treatment: Treatment):
        self.treatment = treatment
        self.recommendation_items = self.get_generic_recommendation()
        self.operation_text = ''
        self.operation_text_if_agree = []

    def prepare_recommendation(self):
        if self.treatment.hematoma_volume:
            if self.treatment.hematoma_volume < 30:
                self.operation_text = low_operation_probability
                self.recommendation_items += [
                    conservative_therapy,
                    CT_angiography,
                    repeated_consultation_if_source_of_hemorrhage,
                ]
            elif 30 < self.treatment.hematoma_volume < 60:
                if not self.treatment.temporary_contraindications and not self.treatment.patient.diagmnoses:
                    self.operation_text = high_operation_probability
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
                else:
                    self.operation_text = high_operation_probability
                    self.recommendation_items += [
                        patient_has_contraindications_for_surgery,
                        dynamic_observation_if_abandonment_of_operation,
                    ]
                    self.operation_text_if_agree += [
                        CT_angiography,
                        repeated_consultation_and_transfer_to_LPU,
                    ]
            else:
                self.operation_text = low_operation_probability_serious_condition_of_patient

    @staticmethod
    def get_generic_recommendation() -> list:
        items = [
            dynamic_observation,
            repeated_CT_and_consultation,
            CT_angiography,
            repeated_neurosurgeon_consultation,
            CT_in_dynamic_through_3_days,
        ]
        return items


def adapt_int_to_patology(num: int, treatment: Treatment):
    int_to_recommendation_link = {
        0: VJK,
        1: VMG_VJK,
        2: VMG_posterior_fossa,
        3: VMG_conservative,
        4: VMG_operation,
        5: Ischemia_conservative,
        6: Ischemia_with_reperfusion,
        7: Tumor,
        8: SAK,
        9: SAK_VMG
    }
    return int_to_recommendation_link[num](treatment)


def get_recommendations(pathologies: list) -> RecommendText:
    recommendations = set()
    operation_text = set()
    operation_text_if_agree = set()

    for patology in pathologies:
        patology.prepare_recommendation()
        recommendations.update(patology.recommendation_items)
        operation_text.update(patology.operation_text)
        operation_text_if_agree.update(patology.operation_text_if_agree)

    recommend = RecommendText.objects.create(operation='.'.join(operation_text),
                                             treatment_tactics=''.join(recommendations),
                                             tactics_if_agree='.'.join(operation_text_if_agree))

    return recommend
