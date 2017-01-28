

#calss header
class _TOOLED():
	def __init__(self,): 
		self.name = "TOOLED"
		self.definitions = [u'Something, especially a piece of leather, that is tooled is covered with decorative patterns using a special tool: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
