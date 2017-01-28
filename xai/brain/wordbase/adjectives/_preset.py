

#calss header
class _PRESET():
	def __init__(self,): 
		self.name = "PRESET"
		self.definitions = [u'arranged, agreed, or chosen earlier: ', u'relating to part of a machine that is used to prepare it to operate or stop later: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
