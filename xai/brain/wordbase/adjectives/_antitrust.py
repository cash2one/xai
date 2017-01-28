

#calss header
class _ANTITRUST():
	def __init__(self,): 
		self.name = "ANTITRUST"
		self.definitions = [u'relating to efforts to prevent companies from working together to control prices unfairly or to create a monopoly (= a single company or group of companies that is the only supplier of something)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
