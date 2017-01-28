

#calss header
class _REWARDING():
	def __init__(self,): 
		self.name = "REWARDING"
		self.definitions = [u'giving a reward, especially by making you feel satisfied that you have done something important or useful, or done something well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
