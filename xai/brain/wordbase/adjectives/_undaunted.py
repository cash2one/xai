

#calss header
class _UNDAUNTED():
	def __init__(self,): 
		self.name = "UNDAUNTED"
		self.definitions = [u'still determined and enthusiastic, despite problems or no success: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
