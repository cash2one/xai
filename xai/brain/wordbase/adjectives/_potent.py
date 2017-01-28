

#calss header
class _POTENT():
	def __init__(self,): 
		self.name = "POTENT"
		self.definitions = [u'very powerful, forceful, or effective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
