

#calss header
class _PLAYABLE():
	def __init__(self,): 
		self.name = "PLAYABLE"
		self.definitions = [u'If a piece of music is playable, it is not too difficult for someone to play.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
