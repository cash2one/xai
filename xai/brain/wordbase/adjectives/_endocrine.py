

#calss header
class _ENDOCRINE():
	def __init__(self,): 
		self.name = "ENDOCRINE"
		self.definitions = [u'relating to any of the organs of the body that make hormones (= chemicals that make the body grow and develop) and put them into the blood, or to the hormones that they make']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
