

from xai.brain.wordbase.nouns._booking import _BOOKING

#calss header
class _BOOKINGS(_BOOKING, ):
	def __init__(self,): 
		_BOOKING.__init__(self)
		self.name = "BOOKINGS"
		self.specie = 'nouns'
		self.basic = "booking"
		self.jsondata = {}
