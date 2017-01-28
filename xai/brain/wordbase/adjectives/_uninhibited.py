

#calss header
class _UNINHIBITED():
	def __init__(self,): 
		self.name = "UNINHIBITED"
		self.definitions = [u'free and natural, without embarrassment or too much control: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
