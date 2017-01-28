

#calss header
class _COMPELLING():
	def __init__(self,): 
		self.name = "COMPELLING"
		self.definitions = [u'If a reason, argument, etc. is compelling, it makes you believe it or accept it because it is so strong: ', u'very exciting and interesting and making you want to watch or listen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
