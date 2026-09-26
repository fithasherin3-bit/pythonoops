class StudentClass:
	def __init__(self):
		self.full_name = None
		self.date_of_birth = None
		self.age = None
		self.gender = None
		self.mobile_number = None
		self.email_address = None
		self.preferred_language = None
		self.school_college_name = None
		self.class_grade = None
		self.board_curriculum = None
		self.academic_year = None
		self.tuition_subjects = []
		self.subject_levels = {}
		self.topics_needing_help = []
		self.parent_guardian_name = None
		self.parent_guardian_relationship = None
		self.parent_guardian_mobile_number = None
		self.parent_guardian_email_address = None
		self.preferred_communication_method = None



	def setusernameandpassword(self, email, password):
			self.email = email
			self.password = password