

#calss header
class _HEREWITH():
	def __init__(self,): 
		self.name = "HEREWITH"
		self.definitions = [u'together with this letter or other official written material: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
