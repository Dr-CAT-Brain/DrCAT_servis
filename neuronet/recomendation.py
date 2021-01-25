from web.models import Treatment
from .recomendation_text import *


class VJK:
    def __init__(self):
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
                        and self.treatment.conscious_level >= 8:
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
    def __init__(self):
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
                        and self.treatment.conscious_level >= 8:
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
        if self.treatment.conscious_level <= 10:
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
