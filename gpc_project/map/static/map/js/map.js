function searchAddressToCoordinate(address) {
    naver.maps.Service.geocode({
        query: address
    }, function(status, response) {
        if (status === naver.maps.Service.Status.ERROR) {
            if (!address) {
                return alert('Geocode Error, Please check address');
            }
            return alert('Geocode Error, address:' + address);
        }

        if (response.v2.meta.totalCount === 0) {
            return alert('No result.');
        }

        var cate = $(".selected").text();

        if (cate === "") {
            return alert('카테고리를 선택해주세요!.');
        }

        var item = response.v2.addresses[0],
            point = new naver.maps.Point(item.x, item.y);

        var geodata = {
            x: item.x,
            y: item.y,
            cate: cate
        }

        $.ajax({
            type: 'GET',
            url: search_url,
            data: geodata,
            success: function(json) {

                if (json.result.status === "fail") {
                    $("#wait_txt").html('아무것도 검색되지 않았습니다..T_T 다른 것을 시도해주세요!');
                    return;
                }
                $("#wait_txt").html('검색완료!');

                removeMarker();

                var MARKER_SPRITE_POSITION = json.result.xy
                var infoWindows = [];

                for (let i = 0; i < MARKER_SPRITE_POSITION.length; i++) {
                    var position = new naver.maps.LatLng(MARKER_SPRITE_POSITION[i][0], MARKER_SPRITE_POSITION[i][1]);
                    var marker = new naver.maps.Marker({
                        position: position,
                        map: map,
                        zIndex: 100
                    });
                    var infoWindow = new naver.maps.InfoWindow({
                        content: '<div style="width:150px;text-align:center;padding:10px;"><b>' + MARKER_SPRITE_POSITION[i][2] + '</b>.<br><a href="' + MARKER_SPRITE_POSITION[i][3] + '" target="_blank">메뉴 보러가기!</a></div>'
                    });

                    markers.push(marker);
                    infoWindows.push(infoWindow);
                };

                naver.maps.Event.addListener(map, 'zoom_changed', function() {
                    updateMarkers(map, markers);
                });

                naver.maps.Event.addListener(map, 'dragend', function() {
                    updateMarkers(map, markers);
                });

                naver.maps.Event.addListener(map, 'idle', function() {
                    updateMarkers(map, markers);
                });

                function getClickHandler(seq) {
                    return function(e) {
                        var marker = markers[seq],
                            infoWindow = infoWindows[seq];

                        if (infoWindow.getMap()) {
                            infoWindow.close();
                        } else {
                            infoWindow.open(map, marker);
                        }
                    }
                }

                function removeMarker() {
                    for (var i = 0; i < markers.length; i++) {
                        markers[i].setMap(null);
                    }
                    markers = [];
                }


                for (var i = 0, ii = markers.length; i < ii; i++) {
                    naver.maps.Event.addListener(markers[i], 'click', getClickHandler(i));
                }

            },
            beforeSend: function() {
                $("#address").val('');
                $("#wait_txt").html('검색 중.. 잠시만 기다려 주십시오..');
                $("#waiting").show();
            },
            complete: function() {

            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

        map.setCenter(point);
    });
}



function initGeocoder() {
    if (!map.isStyleMapReady) {
        return false;
    }
}


function select(ulEl, liEl) {
    Array.from(ulEl.children).forEach(
        v => v.classList.remove('selected')
    )
    if (liEl) liEl.classList.add('selected');
}


function updateMarkers(map, markers) {

    var mapBounds = map.getBounds();
    var marker, position;

    for (var i = 0; i < markers.length; i++) {
        marker = markers[i]
        position = marker.getPosition();

        if (mapBounds.hasLatLng(position)) {
            showMarker(map, marker);
        } else {
            hideMarker(map, marker);
        }
    }
}

function showMarker(map, marker) {
    if (marker.setMap()) return;
    marker.setMap(map);
}

function hideMarker(map, marker) {
    if (!marker.setMap()) return;
    marker.setMap(null);
}