

#calss header
class _ADJUSTABLE():
	def __init__(self,): 
		self.name = "ADJUSTABLE"
		self.definitions = [u'able to be changed to suit particular needs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
