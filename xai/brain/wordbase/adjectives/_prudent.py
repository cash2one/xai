

#calss header
class _PRUDENT():
	def __init__(self,): 
		self.name = "PRUDENT"
		self.definitions = [u'careful and avoiding risks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
