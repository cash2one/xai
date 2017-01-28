

#calss header
class _PROFESSIONAL():
	def __init__(self,): 
		self.name = "PROFESSIONAL"
		self.definitions = [u'relating to work that needs special training or education: ', u'having the qualities that you connect with trained and skilled people, such as effectiveness, skill, organization, and seriousness of manner: ', u'used to describe someone who does a job that people usually do as a hobby: ', u'having the type of job that is respected because it involves a high level of education and training: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
