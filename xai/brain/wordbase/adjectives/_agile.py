

#calss header
class _AGILE():
	def __init__(self,): 
		self.name = "AGILE"
		self.definitions = [u'able to move your body quickly and easily: ', u'able to think quickly and clearly: ', u'used for describing ways of planning and doing work in which it is understood that making changes as they are needed is an important part of the job']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
