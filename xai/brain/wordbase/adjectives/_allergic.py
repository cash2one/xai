

#calss header
class _ALLERGIC():
	def __init__(self,): 
		self.name = "ALLERGIC"
		self.definitions = [u'having an allergy: ', u'caused by an allergy: ', u'having a strong dislike of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
