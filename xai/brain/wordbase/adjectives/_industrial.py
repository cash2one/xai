

#calss header
class _INDUSTRIAL():
	def __init__(self,): 
		self.name = "INDUSTRIAL"
		self.definitions = [u'in or related to industry, or having a lot of industry and factories, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
