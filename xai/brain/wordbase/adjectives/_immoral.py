

#calss header
class _IMMORAL():
	def __init__(self,): 
		self.name = "IMMORAL"
		self.definitions = [u"morally wrong, or outside society's standards of acceptable, honest, and moral behaviour: ", u'money earned from prostitution (= having sex in exchange for money): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
