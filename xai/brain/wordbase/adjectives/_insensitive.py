

#calss header
class _INSENSITIVE():
	def __init__(self,): 
		self.name = "INSENSITIVE"
		self.definitions = [u"not feeling or showing sympathy for other people's feelings, or refusing to give importance to something: ", u'not showing any reaction to something, or unable to feel something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
