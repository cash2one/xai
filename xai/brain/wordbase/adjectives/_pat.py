

#calss header
class _PAT():
	def __init__(self,): 
		self.name = "PAT"
		self.definitions = [u'A pat answer or remark has been previously prepared, so that it is said quickly and without any real thought: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
