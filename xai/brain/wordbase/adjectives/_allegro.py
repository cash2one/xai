

#calss header
class _ALLEGRO():
	def __init__(self,): 
		self.name = "ALLEGRO"
		self.definitions = [u'(played) in a fast and energetic way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
