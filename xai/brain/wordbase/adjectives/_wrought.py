

#calss header
class _WROUGHT():
	def __init__(self,): 
		self.name = "WROUGHT"
		self.definitions = [u'made or done in a careful or decorative way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
