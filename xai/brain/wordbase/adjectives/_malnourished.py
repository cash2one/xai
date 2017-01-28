

#calss header
class _MALNOURISHED():
	def __init__(self,): 
		self.name = "MALNOURISHED"
		self.definitions = [u'weak and in bad health because of having too little food or too little of the types of food necessary for good health']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
