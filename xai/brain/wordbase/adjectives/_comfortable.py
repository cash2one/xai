

#calss header
class _COMFORTABLE():
	def __init__(self,): 
		self.name = "COMFORTABLE"
		self.definitions = [u'Comfortable furniture and clothes provide a pleasant feeling and do not give you any physical problems: ', u'relaxed and free from pain: ', u'If an ill or injured person in hospital is comfortable, they are is not feeling too much pain.', u'If you are comfortable with a situation, you are not worried about it: ', u'having enough money for a good standard of living: ', u'If you win a game or competition by a comfortable amount, you win easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
