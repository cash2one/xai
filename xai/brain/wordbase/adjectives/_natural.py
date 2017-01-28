

#calss header
class _NATURAL():
	def __init__(self,): 
		self.name = "NATURAL"
		self.definitions = [u'as found in nature and not involving anything made or done by people: ', u'A natural ability or characteristic is one that you were born with: ', u'Natural food or drink is pure and has no chemical substances added to it and is therefore thought to be healthy: ', u'a parent who caused someone to be born, although possibly not their legal parent or the parent who raised them', u'normal or expected: ', u'(of a musical note) not sharp or flat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
