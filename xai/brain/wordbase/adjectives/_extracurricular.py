

#calss header
class _EXTRACURRICULAR():
	def __init__(self,): 
		self.name = "EXTRACURRICULAR"
		self.definitions = [u'An extracurricular activity or subject is not part of the usual school or college course.', u'used to refer to something a person does secretly or unofficially and not within their normal work or relationship, especially a sexual relationship: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
