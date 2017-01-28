

#calss header
class _ESTRANGED():
	def __init__(self,): 
		self.name = "ESTRANGED"
		self.definitions = [u'an estranged husband or wife is not now living with the person they are married to: ', u'If you are estranged from your family or friends, you have had a serious argument with them and are no longer friendly with them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
