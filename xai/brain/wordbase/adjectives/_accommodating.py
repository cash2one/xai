

#calss header
class _ACCOMMODATING():
	def __init__(self,): 
		self.name = "ACCOMMODATING"
		self.definitions = [u'used to describe a person who is eager or willing to help other people, for example by changing his or her plans: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
