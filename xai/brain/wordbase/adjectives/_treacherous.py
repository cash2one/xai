

#calss header
class _TREACHEROUS():
	def __init__(self,): 
		self.name = "TREACHEROUS"
		self.definitions = [u'If the ground or sea is treacherous, it is extremely dangerous, especially because of bad weather conditions: ', u'A person who is treacherous deceives someone who trusts them, or has no loyalty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
