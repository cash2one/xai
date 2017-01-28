

#calss header
class _INDELIBLE():
	def __init__(self,): 
		self.name = "INDELIBLE"
		self.definitions = [u'An indelible mark or substance is impossible to remove by washing or in any other way: ', u'Indelible memories or actions are impossible to forget, or have a permanent influence or effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
