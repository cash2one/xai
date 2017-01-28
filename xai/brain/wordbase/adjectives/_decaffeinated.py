

#calss header
class _DECAFFEINATED():
	def __init__(self,): 
		self.name = "DECAFFEINATED"
		self.definitions = [u'Decaffeinated coffee or tea from has had the caffeine (= a chemical substance) removed.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
