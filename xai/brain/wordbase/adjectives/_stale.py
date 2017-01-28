

#calss header
class _STALE():
	def __init__(self,): 
		self.name = "STALE"
		self.definitions = [u'no longer new or fresh, usually as a result of being kept for too long: ', u'not fresh and new; boring because too familiar: ', u'used to describe someone who has lost interest in what they are doing because of being bored or working too hard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
