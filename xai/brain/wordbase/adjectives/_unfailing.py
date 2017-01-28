

#calss header
class _UNFAILING():
	def __init__(self,): 
		self.name = "UNFAILING"
		self.definitions = [u"If a positive quality of someone's character is unfailing, it shows itself at all times: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
