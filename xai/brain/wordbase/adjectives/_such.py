

#calss header
class _SUCH():
	def __init__(self,): 
		self.name = "SUCH"
		self.definitions = [u'used before a noun or noun phrase to add emphasis: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
