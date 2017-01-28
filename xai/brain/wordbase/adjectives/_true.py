

#calss header
class _TRUE():
	def __init__(self,): 
		self.name = "TRUE"
		self.definitions = [u'(especially of facts or statements) right and not wrong; correct: ', u'correct or accurate but not completely explaining something: ', u'being what exists, rather than what was thought, intended, or stated: ', u'If a hope, wish, or dream comes true, it happens although it was unlikely that it would: ', u'sincere or loyal, and likely to continue to be so in difficult situations: ', u'to behave according to your beliefs and do what you think is right', u'Someone who does something true to form or type behaves as other people would have expected from previous experience: ', u'having all the characteristics necessary to be accurately described as something: ', u'fitted or positioned accurately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
