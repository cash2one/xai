

#calss header
class _INDELICATE():
	def __init__(self,): 
		self.name = "INDELICATE"
		self.definitions = [u'Indelicate words or actions are not suitable for a situation and are likely to be offensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
