

#calss header
class _IMPERTINENT():
	def __init__(self,): 
		self.name = "IMPERTINENT"
		self.definitions = [u'rude and not showing respect, especially towards someone older or in a higher position than you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
