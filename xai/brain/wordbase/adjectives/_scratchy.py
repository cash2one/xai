

#calss header
class _SCRATCHY():
	def __init__(self,): 
		self.name = "SCRATCHY"
		self.definitions = [u'A scratchy record, etc. has scratches on it so it makes unpleasant noises when it is played: ', u'Scratchy clothes are rough and uncomfortable.', u'A scratchy pen does not write easily and without interruption: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
