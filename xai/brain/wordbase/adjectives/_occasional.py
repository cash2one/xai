

#calss header
class _OCCASIONAL():
	def __init__(self,): 
		self.name = "OCCASIONAL"
		self.definitions = [u'not happening or done often or regularly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
