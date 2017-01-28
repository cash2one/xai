

#calss header
class _BANEFUL():
	def __init__(self,): 
		self.name = "BANEFUL"
		self.definitions = [u'causing harm or trouble: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
