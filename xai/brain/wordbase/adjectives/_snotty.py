

#calss header
class _SNOTTY():
	def __init__(self,): 
		self.name = "SNOTTY"
		self.definitions = [u'covered with mucus from the nose: ', u'rude and behaving badly, especially by treating other people in a way that shows that you believe yourself to be better than them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
