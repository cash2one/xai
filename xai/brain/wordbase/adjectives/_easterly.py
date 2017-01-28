

#calss header
class _EASTERLY():
	def __init__(self,): 
		self.name = "EASTERLY"
		self.definitions = [u'in or towards the east, or blowing from the east: ', u'a wind that blows from from the east']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
