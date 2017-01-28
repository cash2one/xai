

#calss header
class _ACADEMIC():
	def __init__(self,): 
		self.name = "ACADEMIC"
		self.definitions = [u'relating to schools, colleges, and universities, or connected with studying and thinking, not with practical skills: ', u'used to describe someone who is clever and enjoys studying: ', u'based on ideas and theories and not related to practical effects in real life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
