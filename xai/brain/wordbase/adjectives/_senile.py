

#calss header
class _SENILE():
	def __init__(self,): 
		self.name = "SENILE"
		self.definitions = [u'showing poor mental ability because of old age, especially being unable to think clearly and make decisions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
