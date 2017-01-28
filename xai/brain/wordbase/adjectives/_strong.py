

#calss header
class _STRONG():
	def __init__(self,): 
		self.name = "STRONG"
		self.definitions = [u'powerful; having or using great force or control: ', u'effective; of a good quality or level and likely to be successful: ', u'skilled or good at doing something: ', u'difficult to argue with; firm and determined: ', u'If a taste, smell, etc. is strong, it is very noticeable or powerful: ', u'difficult to break, destroy, or make sick, or able to support a heavy weight or force: ', u'very likely to happen: ', u'having the stated number of people, members, etc.: ', u'A strong acid, alkali, or chemical base produces many ions (= atoms with an electrical charge) when it is dissolved in water.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
