

#calss header
class _SIDEWAYS():
	def __init__(self,): 
		self.name = "SIDEWAYS"
		self.definitions = [u'in a direction to the left or right, not forwards or backwards: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
