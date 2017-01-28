

#calss header
class _BLEARY():
	def __init__(self,): 
		self.name = "BLEARY"
		self.definitions = [u'If you have bleary eyes, your eyes are red or have tears in them and you cannot see clearly, because you are tired or have just woken up: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
