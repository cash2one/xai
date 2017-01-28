

#calss header
class _ENDEMIC():
	def __init__(self,): 
		self.name = "ENDEMIC"
		self.definitions = [u'especially of a disease or a condition, regularly found and very common among a particular group or in a particular area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
