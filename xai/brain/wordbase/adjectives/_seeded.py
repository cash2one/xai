

#calss header
class _SEEDED():
	def __init__(self,): 
		self.name = "SEEDED"
		self.definitions = [u'with the seeds removed: ', u'containing seeds', u'especially of a tennis player, given a place on the list of those expected to win games in a particular competition because of the way they have played in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
