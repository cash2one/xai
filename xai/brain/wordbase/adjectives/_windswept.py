

#calss header
class _WINDSWEPT():
	def __init__(self,): 
		self.name = "WINDSWEPT"
		self.definitions = [u'(of places) open to and not protected from strong winds, or (of people) having hair that is untidy because it has been blown in different directions by the wind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
